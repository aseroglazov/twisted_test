import os

from twisted.protocols.basic import FileSender
from twisted.web.server import NOT_DONE_YET


def download_file(request, name, path, file_is_temp=False):
    file = open(path, 'r')

    def finalize(*args, **kwargs):
        request.finish()
        file.close()
        if file_is_temp:
            os.remove(path)

    request.setHeader('Content-Disposition', 'attachment; filename="{}"'.format(name))

    file_sender = FileSender().beginFileTransfer(file, request)
    file_sender.addCallback(finalize)

    return NOT_DONE_YET
