get_filename_component(ProjectId ${CMAKE_CURRENT_SOURCE_DIR} NAME)

set(LATEX_OUTPUT_PATH "${CMAKE_BINARY_DIR}/bin/")

if ( USE_LATEX )
    message( STATUS "-- " ${ProjectId} )
    file(GLOB_RECURSE report_files "*.tex")

    add_custom_target(
        "${ProjectId}_pdf" ALL
        COMMAND "${Python3_EXECUTABLE}"
        ${CMAKE_SOURCE_DIR}/scripts/convert_tex_to_pdf.py
        ${report_files}
    )

    add_custom_command(
        TARGET ${ProjectId}_pdf
        POST_BUILD
        COMMAND mv ${CMAKE_CURRENT_BINARY_DIR}/*.pdf ${LATEX_OUTPUT_PATH}
    )
else( USE_LATEX )
    message( STATUS "-- ${ProjectId} - NOT BUILD!"  )
endif( USE_LATEX )
