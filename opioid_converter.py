"""Opioid dose converter.

Assumption: Fentanyl input should be provided in micrograms (mcg).
The converter uses 100 mcg IV fentanyl = 10 mg IV morphine.
This equals 30 mg oral morphine.
Thus, 1 mcg fentanyl ~ 0.3 mg oral morphine equivalent (OME).
"""

FENTANYL_TO_OME_MG = 0.3  # mg oral morphine equivalent per mcg fentanyl


def fentanyl_to_ome(fentanyl_mcg: float) -> float:
    """Convert fentanyl dose in micrograms to oral morphine equivalents (mg).

    Parameters
    ----------
    fentanyl_mcg : float
        Dose of fentanyl in micrograms.

    Returns
    -------
    float
        Equivalent dose in oral morphine milligrams.
    """
    return fentanyl_mcg * FENTANYL_TO_OME_MG


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert fentanyl mcg to oral morphine mg.")
    parser.add_argument("mcg", type=float, help="Fentanyl dose in micrograms (mcg)")
    args = parser.parse_args()
    ome = fentanyl_to_ome(args.mcg)
    print(f"{args.mcg} mcg fentanyl is approximately {ome:.2f} mg oral morphine equivalent")

