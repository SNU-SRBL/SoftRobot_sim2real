#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.LinearSolver" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.LinearSolver APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.LinearSolver PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.LinearSolver.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.LinearSolver.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.LinearSolver )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.LinearSolver "${_IMPORT_PREFIX}/lib/Sofa.Component.LinearSolver.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.LinearSolver.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
