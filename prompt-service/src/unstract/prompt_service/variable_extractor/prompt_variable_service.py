import logging
import re
from typing import Any

from unstract.prompt_service.utils.request import HTTPMethod, make_http_request

from .constants import VariableConstants, VariableType

logger = logging.getLogger(__name__)


class VariableService:

    @staticmethod
    def replace_static_variable(
        prompt: str, structured_output: dict[str, Any], variable: str
    ) -> str:
        output_value = VariableService.check_static_variable_run_status(
            structure_output=structured_output, variable=variable
        )
        if not output_value:
            return prompt
        static_variable_marker_string = "".join(["{{", variable, "}}"])

        replaced_prompt: str = VariableService.replace_generic_string_value(
            prompt=prompt, variable=static_variable_marker_string, value=output_value
        )

        return replaced_prompt

    @staticmethod
    def check_static_variable_run_status(
        structure_output: dict[str, Any], variable: str
    ) -> Any:
        output = None
        try:
            output = structure_output[variable]
            return output
        except KeyError:
            logger.warn(
                f"Prompt with {variable} is not executed yet."
                " Unable to replace the variable"
            )
            return output

    @staticmethod
    def replace_generic_string_value(prompt: str, variable: str, value: str) -> str:
        replaced_prompt = re.sub(variable, value, prompt)
        return replaced_prompt

    @staticmethod
    def identify_variable_type(variable: str) -> VariableType:
        variable_type: VariableType
        pattern = re.compile(VariableConstants.DYNAMIC_VARIABLE_URL_REGEX)
        if re.findall(pattern, variable):
            variable_type = VariableType.DYNAMIC
        else:
            variable_type = VariableType.STATIC
        return variable_type

    @staticmethod
    def replace_dynamic_variable(prompt: str, variable: str) -> str:
        url = re.search(VariableConstants.DYNAMIC_VARIABLE_URL_REGEX, variable).group(0)
        data = re.findall(VariableConstants.DYNAMIC_VARIABLE_DATA_REGEX, variable)[0]
        api_response = VariableService.fetch_dynamic_variable_value(url=url, data=data)
        static_variable_marker_string = "".join(["{{", variable, "}}"])
        replaced_prompt: str = VariableService.replace_generic_string_value(
            prompt=prompt, variable=static_variable_marker_string, value=api_response
        )
        return replaced_prompt

    @staticmethod
    def extract_variables_from_prompt(prompt: str) -> list[str]:
        variable: list[str] = []
        variable = re.findall(VariableConstants.VARIABLE_REGEX, prompt)
        return variable

    @staticmethod
    def fetch_dynamic_variable_value(url: str, data: str) -> Any:

        # This prototype method currently supports
        # only endpoints that do not require authentication.
        # Additionally, it only accepts plain text
        # inputs for POST requests in this version.
        # Future versions may include support for
        #  authentication and other input formats.

        verb: HTTPMethod = HTTPMethod.POST
        headers = {"Content-Type": "text/plain"}
        response: Any = make_http_request(
            verb=verb, url=url, data=data, headers=headers
        )
        return response