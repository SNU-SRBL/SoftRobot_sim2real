#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ModelOrderReduction" for configuration "MinSizeRel"
set_property(TARGET ModelOrderReduction APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(ModelOrderReduction PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/ModelOrderReduction.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/ModelOrderReduction.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS ModelOrderReduction )
list(APPEND _IMPORT_CHECK_FILES_FOR_ModelOrderReduction "${_IMPORT_PREFIX}/lib/ModelOrderReduction.lib" "${_IMPORT_PREFIX}/bin/ModelOrderReduction.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
