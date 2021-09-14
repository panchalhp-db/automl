#
# Copyright (C) 2021 Databricks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import unittest

from databricks.automl_runtime.utils import fail_safe_with_default


@fail_safe_with_default(1)
def failed_function():
    raise Exception()


class TestUtilFunctions(unittest.TestCase):
    def test_failed_functions(self):
        result = failed_function()
        self.assertEqual(result, 1)