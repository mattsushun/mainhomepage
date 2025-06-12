# opioid-converter

This project provides a small example converter for opioid dosing. The
assumption used here is that **fentanyl doses should be entered in
micrograms (mcg)**. Internally the conversion assumes 1 mcg of fentanyl is
approximately equivalent to 0.3&nbsp;mg of oral morphine.

Example usage:

```bash
python3 opioid_converter.py 50
```

The command above interprets `50` as `50 mcg` of fentanyl and outputs the
approximate equivalent in oral morphine milligrams.
