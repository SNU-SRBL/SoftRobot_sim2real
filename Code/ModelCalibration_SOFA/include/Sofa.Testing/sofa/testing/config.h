/******************************************************************************
*                 SOFA, Simulation Open-Framework Architecture                *
*                    (c) 2006 INRIA, USTL, UJF, CNRS, MGH                     *
*                                                                             *
* This program is free software; you can redistribute it and/or modify it     *
* under the terms of the GNU Lesser General Public License as published by    *
* the Free Software Foundation; either version 2.1 of the License, or (at     *
* your option) any later version.                                             *
*                                                                             *
* This program is distributed in the hope that it will be useful, but WITHOUT *
* ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       *
* FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License *
* for more details.                                                           *
*                                                                             *
* You should have received a copy of the GNU Lesser General Public License    *
* along with this program. If not, see <http://www.gnu.org/licenses/>.        *
*******************************************************************************
* Authors: The SOFA Team and external contributors (see Authors.txt)          *
*                                                                             *
* Contact information: contact@sofa-framework.org                             *
******************************************************************************/
#pragma once

#include <sofa/config.h>

#define SOFA_TESTING_VERSION 23.06.00

//constexpr std::string with C++20 only
constexpr char SOFA_TESTING_RESOURCES_DIR[] = "J:/0/src/Sofa/framework/Testing/resources";

SOFA_ATTRIBUTE_DEPRECATED("v21.06 (PR#2000)", "v21.12", \
        "Use the compile-time constant SOFA_TESTING_RESOURCES_DIR instead.")
constexpr char FRAMEWORK_TEST_RESOURCES_DIR[] = "J:/0/src/Sofa/framework/Testing/resources";


#ifdef SOFA_BUILD_SOFA_TESTING
#  define SOFA_TARGET Sofa.Testing
#  define SOFA_TESTING_API SOFA_EXPORT_DYNAMIC_LIBRARY
#else
#  define SOFA_TESTING_API SOFA_IMPORT_DYNAMIC_LIBRARY
#endif
