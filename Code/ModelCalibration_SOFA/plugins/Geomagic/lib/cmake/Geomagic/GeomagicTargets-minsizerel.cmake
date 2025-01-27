#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Geomagic" for configuration "MinSizeRel"
set_property(TARGET Geomagic APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Geomagic PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Geomagic.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Geomagic.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Geomagic )
list(APPEND _IMPORT_CHECK_FILES_FOR_Geomagic "${_IMPORT_PREFIX}/lib/Geomagic.lib" "${_IMPORT_PREFIX}/bin/Geomagic.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
