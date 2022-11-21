import pytube

from src.binders.element_binder_base import ElementBinderBase
from src.providers.stream_provider import StreamProvider
from src.ui.url_download_window import Ui_MainWindow


class UrlDownloadWindowBinder(ElementBinderBase):
    __ui_class: Ui_MainWindow

    def __init__(self, ui_class: Ui_MainWindow):
        self.__ui_class = ui_class

    def bind_elements(self):
        self.__ui_class.pushButton_load.clicked.connect(self.__on_load_clicked_handler)

    def __on_stream_progress_handler(self, stream: pytube.Stream, data_chunk: bytes, remaining_bytes: int):
        print(remaining_bytes)

    def __on_stream_finish_handler(self, stream: pytube.Stream, output_path: str):
        print('fin')

    def __populate_streams_dropdown(self, streams: pytube.StreamQuery):
        pass

    def __populate_descriptions(self, yt: pytube.YouTube):
        text: str = ''
        text += yt.title + '\n'
        text += str(yt.views) + ' views' + ' - ' + yt.author
        self.__ui_class.label_video_description.setText(text)

    def __populate_thumbnail(self, thumbnail_url: str):
        pass

    def __on_load_clicked_handler(self):
        url = self.__ui_class.lineEdit_url.text()
        yt = StreamProvider.get_yt(
            video_url=url,
            progress_callback=self.__on_stream_progress_handler,
            complete_callback=self.__on_stream_finish_handler
        )

        self.__populate_descriptions(yt)
        self.__populate_thumbnail(yt.thumbnail_url)
        self.__populate_streams_dropdown(yt.streams)
