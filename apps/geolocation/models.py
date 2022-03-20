from django.db import models


class GeoType:
    PROVINCE = 'province'
    CITY = 'city'
    DISTRICT = 'district'
    VILLAGE = 'village'
    TYPES = (
        (PROVINCE, 'Province'),
        (CITY, 'City'),
        (DISTRICT, 'District'),
        (VILLAGE, 'Village'),
    )


class GeoLocation(models.Model):
    id = models.CharField(max_length=7, primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100, choices=GeoType.TYPES, default=GeoType.PROVINCE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


# class Province(models.Model):
#     id = models.CharField(max_length=2, primary_key=True)
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


# class City(models.Model):
#     id = models.CharField(max_length=5, primary_key=True)
#     name = models.CharField(max_length=255)
#     province = models.ForeignKey(Province, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# class District(models.Model):
#     id = models.CharField(max_length=7, primary_key=True)
#     name = models.CharField(max_length=255)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
