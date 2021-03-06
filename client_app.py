from flask import Blueprint, send_from_directory
import os
import json

client = Blueprint('client', __name__, static_folder="client/build")

@client.route('/', defaults={'path': ''})
@client.route('/<path:path>')
def serve(path):
    print(path)
    if path != "" and os.path.exists(client.static_folder + '/' + path):
        return send_from_directory(client.static_folder, path)
    else:
        return send_from_directory(client.static_folder, 'index.html')    

@client.route("/static/<string:foldername>/<string:filename>")
def serve_static(foldername, filename):
    print(foldername, filename)
    return send_from_directory(client.static_folder+'/static/'+foldername, filename)


# @client.route("/<path:path>")
# def static_proxy(path):
#     """static folder serve"""
#     file_name = path.split("/")[-1]
#     dir_name = os.path.join(client.static_folder, "/".join(path.split("/")[:-1]))
#     return send_from_directory(dir_name, file_name)