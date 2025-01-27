#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.GUI" for configuration "MinSizeRel"
set_property(TARGET Sofa.GUI APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.GUI PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.GUI.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.GUI.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.GUI )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.GUI "${_IMPORT_PREFIX}/lib/Sofa.GUI.lib" "${_IMPORT_PREFIX}/bin/Sofa.GUI.dll" )

# Import target "runSofa" for configuration "MinSizeRel"
set_property(TARGET runSofa APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(runSofa PROPERTIES
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/runSofa.exe"
  )

list(APPEND _IMPORT_CHECK_TARGETS runSofa )
list(APPEND _IMPORT_CHECK_FILES_FOR_runSofa "${_IMPORT_PREFIX}/bin/runSofa.exe" )

# Import target "runSofaGLFW" for configuration "MinSizeRel"
set_property(TARGET runSofaGLFW APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(runSofaGLFW PROPERTIES
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/runSofaGLFW.exe"
  )

list(APPEND _IMPORT_CHECK_TARGETS runSofaGLFW )
list(APPEND _IMPORT_CHECK_FILES_FOR_runSofaGLFW "${_IMPORT_PREFIX}/bin/runSofaGLFW.exe" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
