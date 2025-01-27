#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaPython3Testing" for configuration "MinSizeRel"
set_property(TARGET SofaPython3Testing APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaPython3Testing PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaPython3Testing.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaPython3Testing.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaPython3Testing )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaPython3Testing "${_IMPORT_PREFIX}/lib/SofaPython3Testing.lib" "${_IMPORT_PREFIX}/bin/SofaPython3Testing.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
