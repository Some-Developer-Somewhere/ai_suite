# TODO

## General

### GPT chats

- DB (Flat jsons, etc)
    - https://chat.openai.com/g/g-yYpj7lIby-code-concise-assistant/c/1bb81a29-9d13-401d-8639-2ba2ed2428c9


### Folder structure

```
/my_repository
  /modules
    /models (or /entities or /dtos)
    /speech_recognition
    /text_generation
  /UsageExamples
    /SpeechRecognitionAPI
    /TextGenerationAPI
  /DbService (Fast API (pydantic) which references entities/models)
  /Transcription
  /AI_file_selector
  /StreamlitDashboard
    /pages
        /StartServices (and check if they are not running first)
        /AI_file_selector
        /Transcription
  ...
```

## AI file selector
 
Export root and all open files from VS code
Streamlit:
- Display root and open files
- suggest files to open/close (editor) and/or include/exclude (in prompt context)
 
Maybe a selectable tree with colored suggestions? Collapsed folders where there are no selected or suggested?
 
 
https://youtu.be/-D-M1etGzPw?si=OQGqutsE6urvuQWg
