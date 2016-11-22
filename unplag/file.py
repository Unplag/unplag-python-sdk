"""
This module represents file abstraction in Unplag.
"""

from os.path import splitext
from requests_toolbelt import MultipartEncoder
from msgpack import packb


class File(object):
    """ Representation of file abstact in Unplag """

    def __init__(self, oauth_session, server):
        self.oauth_session = oauth_session
        self.server = server

    def delete(self, id):
        """
        Delete file from library

        :param id: file id in library, string or int
        :return: string
        """
        resp = self.oauth_session.post(self.server + '/api/v2/file/delete', data={'id': id})
        return resp.text

    def get(self, id):
        """
        Get file info from library

        :param id: file id in library, string or int
        :return: string
        """
        resp = self.oauth_session.get(self.server + '/api/v2/file/get?id=%s' % id)
        return resp.text

    def upload(self, path, upload_type='multipart', timeout=600):
        """
        Upload file to library

        :param path: full or absolute path to file
        :param upload_type: allowed upload using 'msgpack', 'multipart' or 'base64'
                            default is multipart
        :param timeout: timeout for uploading file,
                        default is 600 seconds (10 minutes)
        :return: string
        """

        def get_file_extension(path):
            _, file_ext = splitext(path)
            file_ext = file_ext.replace('.', '')
            return file_ext

        file_ext = get_file_extension(path)

        upload_url = self.server + '/api/v2/file/upload'

        # Switch-case for type of upload
        if upload_type == 'multipart':
            file = MultipartEncoder(fields={'format': file_ext, 'file': ('check', open(path, 'rb'), 'application/' + file_ext)})
            resp = self.oauth_session.post(upload_url, data=file, headers={'Content-Type':  file.content_type}, timeout=timeout)

        elif upload_type == 'msgpack':
            file = packb({'format': file_ext, 'file': open(path, 'rb').read()})
            resp = self.oauth_session.post(upload_url, data=file, headers={'Content-Type':  'application/x-msgpack'}, timeout=timeout)

        elif upload_type == 'base64':
            # TODO: implement base64 upload
            raise Exception('Not implemented')
        else:
            raise Exception('Upload type not found!')

        return resp.text
