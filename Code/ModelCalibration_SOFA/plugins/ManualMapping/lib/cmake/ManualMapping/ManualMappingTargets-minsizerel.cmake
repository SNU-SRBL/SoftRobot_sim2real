#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ManualMapping" for configuration "MinSizeRel"
set_property(TARGET ManualMapping APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(ManualMapping PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/ManualMapping.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/ManualMapping.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS ManualMapping )
list(APPEND _IMPORT_CHECK_FILES_FOR_ManualMapping "${_IMPORT_PREFIX}/lib/ManualMapping.lib" "${_IMPORT_PREFIX}/bin/ManualMapping.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
