#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "PluginExample" for configuration "MinSizeRel"
set_property(TARGET PluginExample APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(PluginExample PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/PluginExample.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/PluginExample.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS PluginExample )
list(APPEND _IMPORT_CHECK_FILES_FOR_PluginExample "${_IMPORT_PREFIX}/lib/PluginExample.lib" "${_IMPORT_PREFIX}/bin/PluginExample.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
