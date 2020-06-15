#
# Part of p5: A Python package based on Processing
# Copyright (C) 2017-2019 Abhik Pal
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from enum import Enum

"""Constants Variables for P5 sketches"""

# Environment modes
P2D = "P2D"
P3D = "P3D"

# Stroke Cap Properties
ROUND = "ROUND"
SQUARE = "SQUARE"
PROJECT = "PROJECT"

# Stroke Join Properties
MITER = "MITER"
BEVEL = "BEVEL"
ROUND = "ROUND"

# Ellipse and Rectangle Modes
RADIUS = "RADIUS"
CENTER = "CENTER"
CORNER = "CORNER"
CORNERS = "CORNERS"

# Colors
colour_codes = {
	'indianred': '#CD5C5C',
	'lightcoral': '#F08080',
	'salmon': '#FA8072',
	'darksalmon': '#E9967A',
	'lightsalmon': '#FFA07A',
	'crimson': '#DC143C',
	'red': '#FF0000',
	'firebrick': '#B22222',
	'darkred': '#8B0000',
	'pink': '#FFC0CB',
	'lightpink': '#FFB6C1',
	'hotpink': '#FF69B4',
	'deeppink': '#FF1493',
	'mediumvioletred': '#C71585',
	'palevioletred': '#DB7093',
	'lightsalmon': '#FFA07A',
	'coral': '#FF7F50',
	'tomato': '#FF6347',
	'orangered': '#FF4500',
	'darkorange': '#FF8C00',
	'orange': '#FFA500',
	'gold': '#FFD700',
	'yellow': '#FFFF00',
	'lightyellow': '#FFFFE0',
	'lemonchiffon': '#FFFACD',
	'lightgoldenrodyellow': '#FAFAD2',
	'papayawhip': '#FFEFD5',
	'moccasin': '#FFE4B5',
	'peachpuff': '#FFDAB9',
	'palegoldenrod': '#EEE8AA',
	'khaki': '#F0E68C',
	'darkkhaki': '#BDB76B',
	'lavender': '#E6E6FA',
	'thistle': '#D8BFD8',
	'plum': '#DDA0DD',
	'violet': '#EE82EE',
	'orchid': '#DA70D6',
	'fuchsia': '#FF00FF',
	'magenta': '#FF00FF',
	'mediumorchid': '#BA55D3',
	'mediumpurple': '#9370DB',
	'rebeccapurple': '#663399',
	'blueviolet': '#8A2BE2',
	'darkviolet': '#9400D3',
	'darkorchid': '#9932CC',
	'darkmagenta': '#8B008B',
	'purple': '#800080',
	'indigo': '#4B0082',
	'slateblue': '#6A5ACD',
	'darkslateblue': '#483D8B',
	'mediumslateblue': '#7B68EE',
	'greenyellow': '#ADFF2F',
	'chartreuse': '#7FFF00',
	'lawngreen': '#7CFC00',
	'lime': '#00FF00',
	'limegreen': '#32CD32',
	'palegreen': '#98FB98',
	'lightgreen': '#90EE90',
	'mediumspringgreen': '#00FA9A',
	'springgreen': '#00FF7F',
	'mediumseagreen': '#3CB371',
	'seagreen': '#2E8B57',
	'forestgreen': '#228B22',
	'green': '#008000',
	'darkgreen': '#006400',
	'yellowgreen': '#9ACD32',
	'olivedrab': '#6B8E23',
	'olive': '#808000',
	'darkolivegreen': '#556B2F',
	'mediumaquamarine': '#66CDAA',
	'darkseagreen': '#8FBC8B',
	'lightseagreen': '#20B2AA',
	'darkcyan': '#008B8B',
	'teal': '#008080',
	'aqua': '#00FFFF',
	'cyan': '#00FFFF',
	'lightcyan': '#E0FFFF',
	'paleturquoise': '#AFEEEE',
	'aquamarine': '#7FFFD4',
	'turquoise': '#40E0D0',
	'mediumturquoise': '#48D1CC',
	'darkturquoise': '#00CED1',
	'cadetblue': '#5F9EA0',
	'steelblue': '#4682B4',
	'lightsteelblue': '#B0C4DE',
	'powderblue': '#B0E0E6',
	'lightblue': '#ADD8E6',
	'skyblue': '#87CEEB',
	'lightskyblue': '#87CEFA',
	'deepskyblue': '#00BFFF',
	'dodgerblue': '#1E90FF',
	'cornflowerblue': '#6495ED',
	'mediumslateblue': '#7B68EE',
	'royalblue': '#4169E1',
	'blue': '#0000FF',
	'mediumblue': '#0000CD',
	'darkblue': '#00008B',
	'navy': '#000080',
	'midnightblue': '#191970',
	'cornsilk': '#FFF8DC',
	'blanchedalmond': '#FFEBCD',
	'bisque': '#FFE4C4',
	'navajowhite': '#FFDEAD',
	'wheat': '#F5DEB3',
	'burlywood': '#DEB887',
	'tan': '#D2B48C',
	'rosybrown': '#BC8F8F',
	'sandybrown': '#F4A460',
	'goldenrod': '#DAA520',
	'darkgoldenrod': '#B8860B',
	'peru': '#CD853F',
	'chocolate': '#D2691E',
	'saddlebrown': '#8B4513',
	'sienna': '#A0522D',
	'brown': '#A52A2A',
	'maroon': '#800000',
	'white': '#FFFFFF',
	'snow': '#FFFAFA',
	'honeydew': '#F0FFF0',
	'mintcream': '#F5FFFA',
	'azure': '#F0FFFF',
	'aliceblue': '#F0F8FF',
	'ghostwhite': '#F8F8FF',
	'whitesmoke': '#F5F5F5',
	'seashell': '#FFF5EE',
	'beige': '#F5F5DC',
	'oldlace': '#FDF5E6',
	'floralwhite': '#FFFAF0',
	'ivory': '#FFFFF0',
	'antiquewhite': '#FAEBD7',
	'linen': '#FAF0E6',
	'lavenderblush': '#FFF0F5',
	'mistyrose': '#FFE4E1',
	'gainsboro': '#DCDCDC',
	'lightgray': '#D3D3D3',
	'silver': '#C0C0C0',
	'darkgray': '#A9A9A9',
	'gray': '#808080',
	'dimgray': '#696969',
	'lightslategray': '#778899',
	'slategray': '#708090',
	'darkslategray': '#2F4F4F',
	'black': '#000000',
}

# Shape types / kinds
# POINTS, LINES, TRIANGLES, TRIANGLE_FAN TRIANGLE_STRIP, QUADS, or QUAD_STRIP
class SType(Enum):
	POINTS = 'POINTS'
	LINES = 'LINES'
	TRIANGLES = 'TRIANGLES'
	TRIANGLE_FAN = 'TRIANGLE_FAN'
	TRIANGLE_STRIP = 'TRIANGLE_STRIP'
	QUADS = 'QUADS'
	QUAD_STRIP = 'QUAD_STRIP'
	TESS = 'TESS'
