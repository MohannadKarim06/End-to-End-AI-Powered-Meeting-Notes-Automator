import re
from deepmultilingualpunctuation import PunctuationModel
from spellchecker import SpellChecker
import language_tool_python
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

spell = SpellChecker()
tool = language_tool_python.LanguageTool('en-US')

punc_model = PunctuationModel()



def remove_filler_words(self, text):

    filler_words = ["um", "uh", "you know", "like", "I mean", "so", "well", "hmm", "er", "ah", "right", "okay", "actually", "basically", "kind of", "sort of", "literally", "totally", "just", "really", "yeah", "y'know", "yep", "mhm", "anyway", "see", "look", "listen", "I guess", "I think", "I suppose", "you see", "at the end of the day", "for sure", "in fact", "in general", "more or less", "that said", "to be honest", "to tell you the truth", "I'm telling you", "believe me", "seriously", "frankly", "honestly", "now", "then", "here", "there", "what's more", "furthermore", "moreover", "as a matter of fact", "by the way", "you know what I mean?", "am I right?", "does that make sense?", "got it?", "understand?", "you follow?", "anyways", "anywho", "indeed", "surely", "certainly", "absolutely", "without a doubt", "of course", "no doubt", "for example", "for instance", "in other words", "that is", "namely", "specifically", "in particular", "above all", "after all", "by all means", "in any case", "in short", "to sum up", "all in all", "as I was saying", "as you can see", "as it were", "if you will", "you could say", "one might say", "it's like", "it's as if", "it's just that", "it's worth noting", "it's important to remember", "let me see", "let me think", "hold on", "hang on", "wait a minute", "give me a second", "bear with me", "if I may", "if you don't mind", "if you will allow me", "if I remember correctly", "if I'm not mistaken"]

    pattern = r'\b(' + '|'.join(filler_words) + r')\b'
    text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def remove_repeated_words(self, text):
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    return text


def restore_punctuation(self, text):
    return punc_model.restore_punctuation(text)


def fix_text(text):

    text = " ".join([spell.correction(word) if spell.unknown([word]) else word for word in text.split()])

    matches = tool.check(text)
    for match in matches:
        if match.replacements:
            text = text.replace(match.text, match.replacements[0])

    return text


def remove_small_talk(text):
    """Removes common meeting greetings, chit-chat, filler words, and redundant phrases."""
    small_talk_patterns = [
        r"\b(hello|hi|hey|good morning|good afternoon|good evening|greetings|hiya|howdy|salutations|yo)\b",
        r"\b(how are you|hope you're doing well|how's it going|how are things|how's everyone doing|nice to see you|thanks for joining|thanks for attending|thanks for coming|pleased to meet you|good to see you all|how's your day|how's your week)\b",
        r"\b(yeah|okay|alright|sure|let's start|let's begin|let's get started|sounds good|that's fine|no problem|absolutely|definitely|exactly|great|perfect|wonderful|awesome|fantastic|right|indeed|certainly|surely|affirmative|roger|copy that|agreed|understood|gotcha)\b",
        r"\b(so|well|um|uh|like|you know|I mean|basically|actually|literally|kind of|sort of|just|really|totally|anyhow|anyway|anyways|by the way|er|ah|hmm|y'know|yep|mhm|anywho|see|look|listen|now|then|here|there|yep|mhm|uh-huh|uh huh|mm-hmm|mm hmm|like so)\b",
        r"\b(it's good to be here|I'm happy to be here|I'm glad to be here|it's a pleasure to be here|I'm excited to be here|glad we're all here|happy to join|pleased to be present)\b",
        r"\b(can everyone hear me|can you all hear me|is everyone able to hear me|can you hear me okay|can you hear me all right|is my microphone working|can you see my screen|is my audio clear|test test|testing 1 2 3|mic check|audio check)\b",
        r"\b(sorry I'm late|apologies for being late|I apologize for the delay|excuse my tardiness|sorry for the wait|my apologies|my bad)\b",
        r"\b(thanks for the update|that's great to hear|that's good to know|thanks for sharing|I appreciate the update|thanks for the info|good stuff|thank you for that|appreciate that)\b",
        r"\b(any questions|any thoughts|any comments|anything else to add|does anyone have anything else to say|any feedback|any concerns|any queries|any input)\b",
        r"\b(that's all for today|thanks everyone for attending|thanks for your time|have a great day|have a good one|see you next time|bye everyone|take care|goodbye|farewell|until next time)\b",
        r"\b(I guess|I think|I suppose|you see|at the end of the day|for sure|in fact|in general|more or less|that said|to be honest|to tell you the truth|I'm telling you|believe me|seriously|frankly|honestly|what's more|furthermore|moreover|as a matter of fact|you know what I mean\?|am I right\?|does that make sense\?|got it\?|understand\?|you follow\?|to be fair|in my opinion|personally|from my perspective|if you ask me)\b",
        r"\b(as I was saying|as you can see|as it were|if you will|you could say|one might say|it's like|it's as if|it's just that|it's worth noting|it's important to remember|let me see|let me think|hold on|hang on|wait a minute|give me a second|bear with me|if I may|if you don't mind|if you will allow me|if I remember correctly|if I'm not mistaken|just to clarify|to reiterate|to summarize|to recap|just to add)\b",
        r"\b(literally|totally|just|really|kind of|sort of|basically|actually|you know|I mean|simply|merely)\b", #redundant but helps with frequency
        r"\b(well|so|um|uh|like|right|okay|now then|then again)\b", #redundant but helps with frequency
        r"\b(at the end of the day|for sure|in fact|in general|more or less|that said|to be honest|to tell you the truth|I'm telling you|believe me|seriously|frankly|honestly|to be perfectly honest)\b", #redundant but helps with frequency
        r"\b(anyways|anywho|indeed|surely|certainly|absolutely|without a doubt|of course|no doubt|for example|for instance|in other words|that is|namely|specifically|in particular|above all|after all|by all means|in any case|in short|to sum up|all in all|in summary|in conclusion)\b", #redundant but helps with frequency
        r"\b(i mean to say|it goes without saying|it is what it is|that being said|with that being said|needless to say|to put it simply|to put it another way|to that end|to that effect|as such|in that regard)\b",
        r"\b(correct|exactly right|precisely|spot on|you're right|you're correct|that's correct|you are correct)\b",
        r"\b(right then|alright then|very well|very good|excellent|splendid|fantastic)\b",
        r"\b(for what it's worth|if I may add|if you don't mind me saying|as far as I'm concerned|in my humble opinion)\b",
        r"\b(as you know|as we all know|as mentioned earlier)\b",
        r"\b(moving forward|going forward|in the future|from now on)\b",
        r"\b(with respect to|regarding|concerning|pertaining to)\b",
        r"\b(as previously discussed|as we discussed earlier)\b"
    ]
    for pattern in small_talk_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text


def segment_sentences(text):
    sentences = sent_tokenize(text)
    return " ".join(sentences)


def chunk_text(text, max_length=1024):
    words = text.split()  # Tokenize by whitespace
    chunks = []
    
    for i in range(0, len(words), max_length):
        chunk = " ".join(words[i:i+max_length])
        chunks.append(chunk)
    
    return chunks
    

def preprocess_transcripts(Text):

    text = remove_small_talk(text)
    text = remove_filler_words(text)
    text = remove_repeated_words(text)
    text = fix_text(text)
    text = restore_punctuation(text)
    text = segment_sentences(text)
    chunks = chunk_text(text)

    return chunks
        





