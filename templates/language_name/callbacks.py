#
# #
#                              ITF1788
#
#   Interval Test Framework for IEEE 1788 Standard for Interval Arithmetic
#
#
#   Copyright 2014
#
#   Marco Nehmeier (nehmeier@informatik.uni-wuerzburg.de)
#   Maximilian Kiesner (maximilian.kiesner@stud-mail.uni-wuerzburg.de)
#
#   Department of Computer Science
#   University of Wuerzburg, Germany
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

#
# Input: the string of an integral number as defined in the ITL file
# Output: the required representation for the target test file as a string
#
def cb_int(val):
    return val

#
# Input: the string of a floating point number as defined in the ITL file
# Output: the required representation for the target test file as a string
#
def cb_fpNum(val):
    return val

#
# Input: the string of a qualified identifier as defined in the ITL file
# Output: the required representation for the target test file as a string
#   
def cb_qualident(val):
    return val
