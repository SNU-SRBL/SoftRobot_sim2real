#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.LinearSystem" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.LinearSystem APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.LinearSystem PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.LinearSystem.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.LinearSystem.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.LinearSystem )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.LinearSystem "${_IMPORT_PREFIX}/lib/Sofa.Component.LinearSystem.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.LinearSystem.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
