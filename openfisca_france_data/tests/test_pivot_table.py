# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014, 2015 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from openfisca_france_data.input_data_builders import get_input_data_frame
from openfisca_france_data.surveys import SurveyScenario


def test_pivot_table_1d_mean(year = 2009):
    input_data_frame = get_input_data_frame(year)
    survey_scenario = SurveyScenario().init_from_data_frame(
        input_data_frame = input_data_frame,
        year = year,
        )
    pivot_table = survey_scenario.compute_pivot_table(
        columns = ['decile_rfr'],
        values = ['irpp']
        )
    return pivot_table


def test_pivot_table_1d_sum(year = 2009):
    input_data_frame = get_input_data_frame(year)
    survey_scenario = SurveyScenario().init_from_data_frame(
        input_data_frame = input_data_frame,
        year = year,
        )
    pivot_table = survey_scenario.compute_pivot_table(
        aggfunc = 'sum',
        columns = ['decile_rfr'],
        values = ['irpp']
        )
    return pivot_table


def test_pivot_table_1d_count(year = 2009):
    input_data_frame = get_input_data_frame(year)
    survey_scenario = SurveyScenario().init_from_data_frame(
        input_data_frame = input_data_frame,
        year = year,
        )
    pivot_table = survey_scenario.compute_pivot_table(
        aggfunc = 'count',
        columns = ['decile_rfr'],
        values = ['irpp']
        )
    return pivot_table


def test_pivot_table_2d(year = 2009):
    input_data_frame = get_input_data_frame(year)
    survey_scenario = SurveyScenario().init_from_data_frame(
        input_data_frame = input_data_frame,
        year = year,
        )
    pivot_table = survey_scenario.compute_pivot_table(
        columns = ['decile_rfr'],
        index = ['nbptr'],
        values = ['irpp']
        )
    return pivot_table


if __name__ == '__main__':
    import logging
    import time
    log = logging.getLogger(__name__)
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)

    start = time.time()
    pivot_table = test_pivot_table_1d(year = 2009)
    print time.time() - start
