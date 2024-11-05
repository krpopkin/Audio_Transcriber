# gradio_ui_transcribe.py
import gradio as gr
import file_upload
import transcription_service
import get_the_transcription_results

# Provide only the layout components for the Transcribe tab
def create_transcribe_tab():
    with gr.Blocks() as transcribe_ui:
        # Main layout in two columns: one for file upload and one for transcription info
        with gr.Row():
            # File upload column
            with gr.Column():
                language_input = gr.Textbox(label="Language", interactive=True)
                file_input = gr.File(label="Upload File")
                file_submit_button = gr.Button("Submit")
                upload_output = gr.Textbox(label="Uploaded File", interactive=False)

            # Transcription info column
            with gr.Column():
                transcribe_button = gr.Button("Transcribe")
                check_for_results_button = gr.Button("Check for Transcription Results")
                transcription_output = gr.Textbox(
                    label="Transcript Results",
                    lines=12,
                    max_lines=12,
                    interactive=False,
                    placeholder="Your transcription will appear here"
                )

        # Bind functions to UI elements
        file_submit_button.click(fn=file_upload.upload_file,
                                 inputs=file_input,
                                 outputs=upload_output)
        transcribe_button.click(fn=transcription_service.call_cc_transcription_api,
                                inputs=[upload_output, language_input],
                                outputs=transcription_output)
        check_for_results_button.click(fn=get_the_transcription_results.search_for_transcription,
                                       inputs=transcription_output,
                                       outputs=transcription_output)

    return transcribe_ui
