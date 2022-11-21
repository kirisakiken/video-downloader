import pytube


class StreamProvider:
    @staticmethod
    def get_yt(video_url: str, progress_callback=None, complete_callback=None):
        return pytube.YouTube(
            url=video_url,
            on_progress_callback=progress_callback,
            on_complete_callback=complete_callback,
        )
