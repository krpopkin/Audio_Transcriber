import gradio as gr
import gradio_ui_transcribe
import view_transcripts_functions

def create_gradio_interface():
    with gr.Blocks() as ui:
        gr.Markdown("# Audio Transcription Viewer")

        with gr.Tabs() as tabs:
            # Transcribe Tab - directly use create_transcribe_tab() components
            with gr.Tab("Transcribe"):
                gradio_ui_transcribe.create_transcribe_tab()

            # View Transcripts Tab
            with gr.Tab("View Transcripts"):
                gr.Markdown("### Search for and Display Transcriptions")

                with gr.Row():
                    # Left navigation column for search and dropdown
                    with gr.Column(scale=1, min_width=250) as left_nav:
                        # Initialize dropdown with all titles from the database
                        initial_titles = view_transcripts_functions.filter_titles()
                        title_dropdown = gr.Dropdown(label="Select a Title", choices=initial_titles, interactive=True, value=initial_titles[0] if initial_titles else None)

                    # Main content column for transcription details
                    with gr.Column(scale=3):
                        with gr.Row():
                            language_display = gr.Textbox(label="Language", interactive=False)
                        transcription_output = gr.Textbox(label="Transcription", interactive=False, lines=10)

                # Function to load transcription details based on selected title
                def load_details(title):
                    language, transcription = view_transcripts_functions.load_transcription_details(title)
                    return language, transcription

                # Trigger load_details when a title is selected in the dropdown
                title_dropdown.change(fn=load_details, inputs=title_dropdown, outputs=[language_display, transcription_output])

    return ui
