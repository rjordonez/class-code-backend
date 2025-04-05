import azure.cognitiveservices.speech as speechsdk

# 🗝️ Replace with your values
speech_key = "CPhzqHVeoa5YnFTLqimhoVB8tiM0aYdtnAnumfNJtVkv3AzHV18PJQQJ99BDACYeBjFXJ3w3AAAYACOGaN2q"
region = "eastus"
audio_file = "sample.wav"

# 🔧 Set up config
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=region)
audio_config = speechsdk.AudioConfig(filename=audio_file)

# 🎯 Configure pronunciation assessment (unscripted mode)
pron_config = speechsdk.PronunciationAssessmentConfig(
    reference_text="",
    grading_system=speechsdk.PronunciationAssessmentGradingSystem.HundredMark,
    granularity=speechsdk.PronunciationAssessmentGranularity.Phoneme,
    enable_miscue=True
)

# ✅ Set phoneme alphabet AFTER initialization
pron_config.phoneme_alphabet = "IPA"  # <- must be a string: "IPA" or "SAPI"
pron_config.enable_prosody_assessment()
pron_config.n_best_phoneme_count = 5

# 🎙️ Recognizer
recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
pron_config.apply_to(recognizer)

# 🚀 Run recognition
result = recognizer.recognize_once()

# 📄 Print result JSON
json_result = result.properties.get(speechsdk.PropertyId.SpeechServiceResponse_JsonResult)
print(json_result)