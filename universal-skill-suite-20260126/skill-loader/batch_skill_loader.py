import os
import sys
import argparse
import tkinter as tk
from tkinter import ttk, messagebox

def load_skills(base_dir, output_file="combined-skills.md", folders=None):
    """
    递归遍历指定目录下的所有子文件夹（或指定文件夹），读取每个文件夹中的 SKILL.md 文件，
    并将它们合并成一个系统提示文件。支持增量合并，避免重复。
    """
    output_path = os.path.join(base_dir, output_file)
    existing_prompt = ""
    existing_skills = set()

    # 读取现有 combined-skills.md，如果存在
    if os.path.exists(output_path):
        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                existing_prompt = f.read()
            # 解析现有技能
            sections = existing_prompt.split("--- ")
            for section in sections[1:]:  # 跳过第一个空
                if section.strip():
                    lines = section.split("\n", 1)
                    skill_name = lines[0].strip()
                    existing_skills.add(skill_name)
        except Exception as e:
            print(f"读取现有 {output_path} 时出错: {e}")

    combined_prompt = existing_prompt
    skill_count = len(existing_skills)

    # 确定要遍历的文件夹
    if folders:
        target_folders = folders
    else:
        target_folders = []
        for root, dirs, files in os.walk(base_dir):
            for dir_name in dirs:
                if dir_name != os.path.basename(output_file).replace('.md', ''):  # 避免处理输出文件目录
                    target_folders.append(os.path.relpath(os.path.join(root, dir_name), base_dir))

    # 遍历目标文件夹
    for folder_rel in target_folders:
        folder_path = os.path.join(base_dir, folder_rel)
        if os.path.isdir(folder_path):
            skill_md_path = os.path.join(folder_path, "SKILL.md")
            if os.path.exists(skill_md_path):
                folder_name = folder_rel.replace(os.sep, '-').replace('/', '-')  # 用-替换路径分隔符作为skill名称
                if folder_name in existing_skills:
                    print(f"Skill {folder_name} 已存在，跳过")
                    continue
                try:
                    with open(skill_md_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    combined_prompt += f"--- {folder_name} ---\n{content}\n\n"
                    skill_count += 1
                    print(f"已加载新 skill: {folder_name}")
                except Exception as e:
                    print(f"读取 {skill_md_path} 时出错: {e}")
            else:
                print(f"文件夹 {folder_rel} 中未找到 SKILL.md，跳过")
        else:
            print(f"指定的文件夹 {folder_rel} 不存在")

    if skill_count == 0:
        print("未找到任何 SKILL.md 文件。")
        return

    # 输出到文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(combined_prompt)

    print(f"合并完成！共加载 {skill_count} 个 skill。输出文件: {output_path}")
    messagebox.showinfo("完成", f"合并完成！共加载 {skill_count} 个 skill。\n输出文件: {output_path}")

def collect_skills_from_folder(base_dir, folder_rel):
    """
    从指定文件夹递归收集所有SKILL.md的相对路径。
    """
    skills = []
    folder_path = os.path.join(base_dir, folder_rel)
    for root, dirs, files in os.walk(folder_path):
        if "SKILL.md" in files:
            rel_path = os.path.relpath(root, base_dir)
            skills.append(rel_path)
    return skills

def start_gui(base_dir, output_file):
    """
    启动可视化界面，像资源管理器一样显示文件夹树，让用户选择文件夹。
    选择父文件夹会递归合并子文件夹的skill。
    """
    root = tk.Tk()
    root.title("Skill 合并工具")
    root.geometry("600x500")

    # 创建树状视图
    tree = ttk.Treeview(root, selectmode="none")
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    last_selected = None

    # 绑定点击事件，实现按钮式选择，支持Shift范围
    def on_tree_click(event):
        nonlocal last_selected
        item = tree.identify_row(event.y)
        if item:
            if event.state & 0x1:  # Shift pressed
                if last_selected:
                    # 范围选择
                    items = tree.get_children()
                    try:
                        start_idx = items.index(last_selected)
                        end_idx = items.index(item)
                        if start_idx > end_idx:
                            start_idx, end_idx = end_idx, start_idx
                        for i in range(start_idx, end_idx + 1):
                            tree.selection_add(items[i])
                    except ValueError:
                        pass
                else:
                    tree.selection_add(item)
            else:
                if item in tree.selection():
                    tree.selection_remove(item)
                else:
                    tree.selection_add(item)
            last_selected = item

    tree.bind("<Button-1>", on_tree_click)

    # 定义图标（可选）
    tree.heading("#0", text="文件夹结构")

    # 递归构建树
    def build_tree(parent, path, rel_path=""):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                item_rel = os.path.join(rel_path, item) if rel_path else item
                node = tree.insert(parent, "end", text=item, values=(item_rel,))
                build_tree(node, item_path, item_rel)

    build_tree("", base_dir)

    # 按钮
    def execute():
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showwarning("警告", "请至少选择一个文件夹！")
            return
        selected_folders = []
        for item in selected_items:
            folder_rel = tree.item(item, "values")[0]
            if folder_rel:
                # 递归收集该文件夹下的所有skill
                skills = collect_skills_from_folder(base_dir, folder_rel)
                selected_folders.extend(skills)
        if not selected_folders:
            messagebox.showwarning("警告", "选中的文件夹中未找到SKILL.md！")
            return
        load_skills(base_dir, output_file, selected_folders)
        root.destroy()

    tk.Button(root, text="执行合并", command=execute).pack(pady=10)
    tk.Button(root, text="退出", command=root.quit).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="批量加载 skill 文件夹中的 SKILL.md 并合并为系统提示。")
    parser.add_argument("--dir", default=os.getcwd(), help="指定 skill 文件夹的根目录（默认当前目录）")
    parser.add_argument("--output", default="combined-skills.md", help="输出文件名（默认 combined-skills.md）")
    parser.add_argument("--folders", nargs="*", help="指定要遍历的文件夹名（多个用空格分隔，使用此参数时使用命令行模式）")

    args = parser.parse_args()

    if args.folders:
        # 命令行模式
        load_skills(args.dir, args.output, args.folders)
    else:
        # GUI 模式
        start_gui(args.dir, args.output)