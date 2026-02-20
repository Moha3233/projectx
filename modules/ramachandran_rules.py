class RamachandranValidator:

    def validate(self, sequence):
        violations = 0

        for aa in sequence:
            if aa == "P":  # Proline restriction
                violations += 1
            if aa == "G":  # Glycine flexible
                continue

        compliance = 1 - (violations / len(sequence))
        return compliance
