#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaGeneralExplicitOdeSolver" for configuration "MinSizeRel"
set_property(TARGET SofaGeneralExplicitOdeSolver APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaGeneralExplicitOdeSolver PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaGeneralExplicitOdeSolver.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaGeneralExplicitOdeSolver.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaGeneralExplicitOdeSolver )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaGeneralExplicitOdeSolver "${_IMPORT_PREFIX}/lib/SofaGeneralExplicitOdeSolver.lib" "${_IMPORT_PREFIX}/bin/SofaGeneralExplicitOdeSolver.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
