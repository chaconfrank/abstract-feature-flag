from calculate_minimum_preparation_time import CalculateMinimumPreparationTime, CalculateMinimumPreparationTimeOld, \
    FactoryCalculateMinimumPreparationTime
from feature_flag import FeatureFlag


class FeatureFactoryCalculateMinimumPreparationTime:

    def __init__(self):
        self.hash_map = {
            True: CalculateMinimumPreparationTime(),
            False: CalculateMinimumPreparationTimeOld()
        }

    def get_factory(self, feature_flag: str) -> FactoryCalculateMinimumPreparationTime:
        is_active = FeatureFlag.is_active(feature_flag)
        return self.hash_map[is_active]
