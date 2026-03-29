# Analysis

## Layer 2, Head 1

This head appears to be a "Next-Token" or "Look-Ahead" head. In the attention diagrams, there is a clear, bright diagonal line shifted exactly one square to the right of the main diagonal. This indicates that each word is primarily paying attention to the token that immediately follows it in the sentence structure.

Example Sentences:
The [MASK] sat on the mat.
A [MASK] barked loudly at the mailman.

## Layer 1, Head 5

This head functions as a "Delimiter" or "Separator" specialist. The diagram shows a very distinct, bright vertical column on the far right edge, specifically under the [SEP] token. Regardless of which word is in the row, the model "parks" its attention on the end-of-sentence marker. This suggests the head is used to maintain a global or "null" state when no specific local grammatical relationship is found.

Example Sentences:
The quick brown fox jumps over the [MASK].
Artificial intelligence is a [MASK] of computer science.

