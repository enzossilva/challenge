from flask import request, redirect, url_for
from app.models import start_scan_models, get_scan_results
from app.view import render_index, render_list_scan


def index():
    return render_index()


def start_scan_controller():
    target_url = f'https://{request.form["target_url"]}'
    start_scan_models(target_url)
    return redirect(url_for("list_scan_route", url=request.form["target_url"]))


def list_scan_controller(target_url):
    target_url = f'https://{target_url}'
    results = get_scan_results(target_url)
    return render_list_scan(results)

