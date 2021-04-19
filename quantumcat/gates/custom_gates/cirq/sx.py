# (C) Copyright Artificial Brain 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import cirq
import numpy


class SX(cirq.Gate):
    def __init__(self, theta):
        super(SX, self).__init__()
        self.theta = theta

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        return numpy.array([[1 + 1j, 1 - 1j],
                            [1 - 1j, 1 + 1j]]) / 2

    def _circuit_diagram_info_(self, args):
        return "SX"
