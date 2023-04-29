
class FeatureFlag:

    @staticmethod
    def is_active(key: str) -> bool:
        is_active = False
        if key == 'calculate':
            is_active = True

        return is_active
