from feature_factory import FeatureFactoryCalculateMinimumPreparationTime


def main():
    result = FeatureFactoryCalculateMinimumPreparationTime()\
        .get_factory(feature_flag='calculate-old')\
        .execute(batch={'code': '0001'})
    print(result)


if __name__ == "__main__":
    main()
