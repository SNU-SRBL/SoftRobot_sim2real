#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaPython3::Bindings.SofaGui" for configuration "MinSizeRel"
set_property(TARGET SofaPython3::Bindings.SofaGui APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaPython3::Bindings.SofaGui PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Gui.lib"
  IMPORTED_LINK_DEPENDENT_LIBRARIES_MINSIZEREL "Python::Python"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Gui.cp38-win_amd64.pyd"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaPython3::Bindings.SofaGui )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaPython3::Bindings.SofaGui "${_IMPORT_PREFIX}/lib/Gui.lib" "${_IMPORT_PREFIX}/bin/Gui.cp38-win_amd64.pyd" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
