#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.Playback" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.Playback APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.Playback PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.Playback.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.Playback.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.Playback )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.Playback "${_IMPORT_PREFIX}/lib/Sofa.Component.Playback.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.Playback.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
