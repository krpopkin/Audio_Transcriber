import gradio_ui_transcribe
import gradio_ui_view_transcripts

if __name__ == '__main__':
    #interface = gradio_ui_transcribe.create_gradio_interface()
    interface = gradio_ui_view_transcripts.create_gradio_interface()
    interface.launch(share=False)
