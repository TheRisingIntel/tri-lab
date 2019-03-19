from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from adhocracy4.comments import models as comment_models
from adhocracy4.maps import fields as map_fields
from adhocracy4.ratings import models as rating_models
from liqd_product.apps.ideas import models as idea_models


class AbstractMapIdea(idea_models.AbstractIdea):
    point = map_fields.PointField(
        verbose_name=_('Where can your idea be located on a map?'),
        help_text=_('Click inside the marked area '
                    'or type in an address to set the marker. A set '
                    'marker can be dragged when pressed.'))

    point_label = models.CharField(
        blank=True,
        default='',
        max_length=255,
        verbose_name=_('Label of the ideas location'),
        help_text=_('This could be an address or the name of a landmark.'),
    )

    class Meta:
        abstract = True


class MapIdea(AbstractMapIdea):
    ratings = GenericRelation(rating_models.Rating,
                              related_query_name='mapidea',
                              object_id_field='object_pk')
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='mapidea',
                               object_id_field='object_pk')

    def get_absolute_url(self):
        return reverse(
            'liqd_product_mapideas:mapidea-detail',
            kwargs=dict(
                partner_slug=self.project.organisation.partner.slug,
                pk='{:05d}'.format(self.pk),
                year=self.created.year
            )
        )

    class Meta:
        ordering = ['-created']
        verbose_name = 'mapidea'
        db_table = 'meinberlin_mapideas_mapidea'