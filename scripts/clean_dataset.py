import os
import shutil
import pydot
import json
from tqdm import tqdm

def has_cfg_edges(filepath):
    """Check if the graph has any CFG-related edges."""
    try:
        graphs = pydot.graph_from_dot_file(filepath)
        if not graphs:
            return False
        edges = graphs[0].get_edges()
        for edge in edges:
            label = edge.get('label')
            if label and "cfg" in label.lower():
                return True
        return False
    except Exception as e:
        print(f"[!] Failed to check CFG in {filepath}: {e}")
        return False

def count_nodes(filepath):
    """Accurate node count using pydot."""
    try:
        graphs = pydot.graph_from_dot_file(filepath)
        if graphs:
            nodes = graphs[0].get_nodes()
            real_nodes = [n for n in nodes if n.get_name() not in ('node', 'graph', 'edge')]
            return len(real_nodes)
    except Exception as e:
        print(f"[!] Failed to count nodes in {filepath}: {e}")
    return 0

def copy_valid_graphs(input_folder, output_folder, max_nodes=500):
    """Copy only graphs with ≤ max_nodes and having at least one CFG edge. Log removed files."""
    os.makedirs(output_folder, exist_ok=True)

    dot_files = [f for f in os.listdir(input_folder) if f.endswith(".dot")]

    kept = 0
    skipped_size = 0
    skipped_cfg = 0
    skipped_fail = 0

    removed_files = {
        "too_many_nodes": [],
        "no_cfg": [],
        "read_error": []
    }

    for file in tqdm(dot_files, desc="Filtering graphs"):
        input_path = os.path.join(input_folder, file)

        try:
            node_count = count_nodes(input_path)
            if node_count > max_nodes:
                skipped_size += 1
                removed_files["too_many_nodes"].append(file)
                continue
            if not has_cfg_edges(input_path):
                skipped_cfg += 1
                removed_files["no_cfg"].append(file)
                continue

            shutil.copy(input_path, os.path.join(output_folder, file))
            kept += 1
        except Exception as e:
            print(f"[!] Failed to process {file}: {e}")
            skipped_fail += 1
            removed_files["read_error"].append(file)

    # Save JSON log
    log_path = os.path.join(output_folder, "removed_files_log.json")
    with open(log_path, "w") as f:
        json.dump(removed_files, f, indent=2)

    # Summary
    total = len(dot_files)
    print("\n=== Filtering Summary ===")
    print(f"[📊] Total input files: {total}")
    print(f"[✓] Kept (valid): {kept} ({kept / total * 100:.2f}%)")
    print(f"[✂️] Skipped (too many nodes >{max_nodes}): {skipped_size} ({skipped_size / total * 100:.2f}%)")
    print(f"[✂️] Skipped (no CFG edges): {skipped_cfg} ({skipped_cfg / total * 100:.2f}%)")
    print(f"[⚠️] Skipped (read errors): {skipped_fail} ({skipped_fail / total * 100:.2f}%)")
    print(f"[📝] Removed files logged to: {log_path}")

if __name__ == "__main__":
    input_dir = "cpgs/chrome"       # Your input folder
    output_dir = "cpgs/c_chrome"    # Your output folder (cleaned graphs)

    copy_valid_graphs(input_dir, output_dir, max_nodes=500)
