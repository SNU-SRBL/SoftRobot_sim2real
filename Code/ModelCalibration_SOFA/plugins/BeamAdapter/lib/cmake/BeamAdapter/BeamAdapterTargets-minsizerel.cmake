#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "BeamAdapter" for configuration "MinSizeRel"
set_property(TARGET BeamAdapter APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(BeamAdapter PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/BeamAdapter.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/BeamAdapter.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS BeamAdapter )
list(APPEND _IMPORT_CHECK_FILES_FOR_BeamAdapter "${_IMPORT_PREFIX}/lib/BeamAdapter.lib" "${_IMPORT_PREFIX}/bin/BeamAdapter.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
