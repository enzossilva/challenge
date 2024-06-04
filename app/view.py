from flask import render_template


def render_index():
    return render_template("index.html")


def render_list_scan(results):
    return render_template("list_scan.html", list_scans=results)
