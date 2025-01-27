#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.LinearSolver.Preconditioner" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.LinearSolver.Preconditioner APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.LinearSolver.Preconditioner PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.LinearSolver.Preconditioner.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.LinearSolver.Preconditioner.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.LinearSolver.Preconditioner )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.LinearSolver.Preconditioner "${_IMPORT_PREFIX}/lib/Sofa.Component.LinearSolver.Preconditioner.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.LinearSolver.Preconditioner.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
