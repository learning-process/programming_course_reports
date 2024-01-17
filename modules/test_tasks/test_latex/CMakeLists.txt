get_filename_component(ProjectId ${CMAKE_CURRENT_SOURCE_DIR} NAME)

set(LATEX_OUTPUT_PATH "${CMAKE_BINARY_DIR}/bin/")

if ( USE_LATEX AND LATEX_FOUND AND LATEX_PDFLATEX_FOUND )
    message( STATUS "-- " ${ProjectId} )
    file(GLOB_RECURSE report_files "*.tex")

#    get_filename_component(report_names ${report_files} NAME)
#    add_latex_document(${report_names})

#    if (NOT TARGET ${ProjectId}_pdf)
#        add_custom_command(
#                TARGET ${ProjectId}_pdf
#                POST_BUILD
#                COMMAND rm ${LATEX_OUTPUT_PATH}/*.aux
#                COMMAND rm ${LATEX_OUTPUT_PATH}/*.log
#                COMMAND rm ${LATEX_OUTPUT_PATH}/*.tex
#        )
#    endif()

    # First pass.
    ADD_CUSTOM_TARGET( ${ProjectId}_prebuild
            COMMAND ${PDFLATEX_COMPILER}  -output-directory ${LATEX_OUTPUT_PATH} -draftmode -interaction=nonstopmode ${report_files}
            COMMENT "Starting Prebuild."
            WORKING_DIRECTORY ${WORKINGDIR}
            DEPENDS ${report_files})

    # Second pass - generate the final pdf.
    ADD_CUSTOM_TARGET( ${ProjectId}_pdf
            COMMAND ${PDFLATEX_COMPILER} -output-directory ${LATEX_OUTPUT_PATH}  ${report_files}
            WORKING_DIRECTORY ${WORKINGDIR}
            COMMENT "Assembling the final pdf file."
            DEPENDS  ${report_files})

    ADD_CUSTOM_TARGET(${ProjectId}_all_formats ALL) # Entry point of execution.
    ADD_DEPENDENCIES(${ProjectId}_all_formats ${ProjectId}_pdf)

else()
    message( STATUS "-- ${ProjectId} - NOT BUILD!"  )
endif()
