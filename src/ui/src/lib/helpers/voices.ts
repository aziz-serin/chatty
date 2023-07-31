export const voices: any = {
    "Arabic": {"Male": "ar-XA-Wavenet-B", "Female": "ar-XA-Wavenet-A"},
    "Chinese (Mandarin)": {"Male": "cmn-CN-Wavenet-B", "Female": "cmn-CN-Wavenet-A"},
    "Dutch": {"Male": "nl-NL-Wavenet-B", "Female": "nl-NL-Wavenet-A"},
    "English": {"Male": "en-GB-Wavenet-B", "Female": "en-GB-Wavenet-A"},
    "French": {"Male": "fr-FR-Wavenet-B", "Female": "fr-FR-Wavenet-A"},
    "German": {"Male": "de-DE-Wavenet-B", "Female": "de-DE-Wavenet-A"},
    "Italian": {"Male": "it-IT-Wavenet-B", "Female": "it-IT-Wavenet-A"},
    "Japanese": {"Male": "ja-JP-Wavenet-B", "Female": "ja-JP-Wavenet-A"},
    "Polish": {"Male": "pl-PL-Wavenet-B", "Female": "pl-PL-Wavenet-A"},
    "Portuguese": {"Male": "cpt-PT-Wavenet-B", "Female": "pt-PT-Wavenet-A"},
    "Russian": {"Male": "ru-RU-Wavenet-B", "Female": "ru-RU-Wavenet-A"},
    "Spanish": {"Male": "es-ES-Wavenet-B", "Female": "es-ES-Wavenet-C"},
    "Turkish": {"Male": "tr-TR-Wavenet-B", "Female": "tr-TR-Wavenet-A"},
};

export let languages: string[] = [
    "Arabic",
    "Chinese (Mandarin)",
    "Dutch",
    "English",
    "French",
    "German",
    "Italian",
    "Japanese",
    "Polish",
    "Portuguese",
    "Russian",
    "Spanish",
    "Turkish"
];

export function selectVoiceFromOptions(language: string, gender: string): string {
    return voices[language][gender];
}
