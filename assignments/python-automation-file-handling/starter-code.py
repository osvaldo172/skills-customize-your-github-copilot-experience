def read_text_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def count_text_metrics(text):
    lines = text.splitlines()
    words = text.split()
    characters = len(text)
    return {
        "lines": len(lines),
        "words": len(words),
        "characters": characters,
    }


def write_report(path, metrics):
    report_lines = [
        "File Analysis Report",
        "---------------------",
        f"Lines: {metrics['lines']}",
        f"Words: {metrics['words']}",
        f"Characters: {metrics['characters']}",
    ]
    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(report_lines))
    return path


def append_log(path, message):
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {message}\n")
    return path


def main():
    source_path = "sample-notes.txt"
    report_path = "report.txt"
    log_path = "automation-log.txt"

    text = read_text_file(source_path)
    metrics = count_text_metrics(text)
    write_report(report_path, metrics)

    summary = (
        f"Processed {source_path}: {metrics['lines']} lines, "
        f"{metrics['words']} words, {metrics['characters']} characters"
    )
    append_log(log_path, summary)

    print(f"Report saved to {report_path}")
    print(f"Log updated in {log_path}")


if __name__ == "__main__":
    main()
