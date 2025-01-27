#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "image_gui" for configuration "MinSizeRel"
set_property(TARGET image_gui APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(image_gui PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/image_gui.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/image_gui.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS image_gui )
list(APPEND _IMPORT_CHECK_FILES_FOR_image_gui "${_IMPORT_PREFIX}/lib/image_gui.lib" "${_IMPORT_PREFIX}/bin/image_gui.dll" )

# Import target "image" for configuration "MinSizeRel"
set_property(TARGET image APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(image PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/image.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/image.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS image )
list(APPEND _IMPORT_CHECK_FILES_FOR_image "${_IMPORT_PREFIX}/lib/image.lib" "${_IMPORT_PREFIX}/bin/image.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
