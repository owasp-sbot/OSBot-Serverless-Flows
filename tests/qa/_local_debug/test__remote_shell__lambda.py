import os
from unittest                                                       import TestCase

import pytest

from osbot_utils.utils.Files import file_from_bytes, file_exists, folder_exists, folder_files
from osbot_utils.utils.Misc                                         import base64_to_bytes
from osbot_serverless_flows.utils._for_osbot_aws.Http__Remote_Shell import Http__Remote_Shell
from tests.qa.for_qa_tests                                          import qa__endpoint_url


@pytest.mark.skip("only used for manual testing")
class test_remote_shell_lambda(TestCase):

    def setUp(self):
        self.port  = 5002
        self.target_server = qa__endpoint_url
        self.target_url = f'{self.target_server}/debug/lambda-shell'
        self.shell = Http__Remote_Shell(target_url=self.target_url)

    def test_0_lambda_shell_setup(self):
        assert self.shell.ping() == 'pong'


    def test_1_ping(self):
        def return_value():
            return 'here....'
        assert self.shell.function(return_value) == 'here....'


    # def test_connection_with_prefect_server(self):
    #     def connection_with_prefect_server():
    #         import osbot_utils
    #         return f"{osbot_utils}"
    #
    #     self.shell.function__print(connection_with_prefect_server)

    # older test

    # def test_2_playwright__install_chrome(self):
    #     def playwright__install_chrome():
    #         from osbot_playwright.playwright.api.Playwright_CLI import Playwright_CLI
    #         playwright_cli = Playwright_CLI()
    #         result = playwright_cli.browser_installed__chrome()
    #         if result is False:
    #             result = playwright_cli.install__chrome()
    #         return f'{result}'
    #
    #     install_result           = self.shell.function(playwright__install_chrome)
    #     assert install_result   == 'True'

    # def test_2_load_browser(self):
    #     def playwright__check_browser():
    #         from osbot_utils.utils.Files                                  import folder_files, file_exists, folder_exists
    #         from osbot_serverless_flows.playwright.Playwright__Serverless import Playwright__Serverless
    #         from osbot_utils.utils.Threads                                import invoke_in_new_event_loop
    #         from osbot_playwright.playwright.api.Playwright_CLI           import Playwright_CLI
    #         async def run_checks():
    #
    #             playwright_cli = Playwright_CLI()
    #             with Playwright__Serverless() as _:
    #                 #await _.launch()
    #                 #result = playwright_cli.invoke_raw(['install', 'chromium'])
    #                 #return result
    #                 return folder_files(playwright_cli.install_location('chromium'))
    #                 result = dict(browser_exists           = _.browser__exists()                        ,
    #                               file_exists             = file_exists(_.chrome_path())                ,
    #                               chrome_path              = _.chrome_path()                            ,
    #                               install_location         = playwright_cli.install_location('chromium'),
    #                               folder_exists            = folder_exists(playwright_cli.install_location('chromium')),
    #                               executable_path__chrome  = playwright_cli.executable_path__chrome()   ,
    #                               browser                  =  f'{type(_.browser)}'                      )
    #                 return result
    #
    #
    #         return invoke_in_new_event_loop(run_checks())
    #
    #     self.shell.function__print(playwright__check_browser)
    #
    # def test_3_run_playwright__page_screenshot(self):
    #
    #     def playwright__page_screenshot():
    #         from osbot_utils.utils.Threads import async_invoke_in_new_loop
    #         from osbot_utils.utils.Misc    import bytes_to_base64
    #         from playwright.async_api      import async_playwright
    #         from osbot_playwright.playwright.api.Playwright_CLI import Playwright_CLI
    #         playwright_cli = Playwright_CLI()
    #         chrome_path    = playwright_cli.executable_path__chrome()
    #
    #         async def get_screenshot(url):
    #             context = await async_playwright().start()
    #             launch_kwargs = dict(args            =["--disable-gpu", "--single-process"],
    #                                  executable_path = chrome_path                         )
    #             browser = await context.chromium.launch(**launch_kwargs)
    #             page    = await browser.new_page()
    #             await page.goto                 (url)
    #
    #             screenshot = await page.screenshot(full_page=True)
    #             return bytes_to_base64(screenshot)
    #
    #         target_url = "https://www.google.com/news"
    #         return async_invoke_in_new_loop(get_screenshot(url=target_url))
    #
    #     screenshot_base64 = self.shell.function(playwright__page_screenshot)
    #     screenshot_bytes  = base64_to_bytes(screenshot_base64)
    #
    #     assert len(screenshot_base64)   > 8000
    #     assert type(screenshot_bytes)   is bytes
    #
    #     print(file_from_bytes(bytes=screenshot_bytes, extension='.png'))
    #
    # def test_4_check_new_osbot_threading_async_execution(self):                 # test running on my local dev laptop
    #
    #     def execute_in_lambda():                                              # sync function that will be executed in AWS Lambda
    #         import asyncio                                                    # these imports are needed since this code is executed inside ...
    #         from osbot_utils.utils.Threads import async_invoke_in_new_loop    #    a code environment that doesn't have those imports
    #
    #         async def an_async_function():                                    # async function to execute from a sync function (which is REALLY hard to do)
    #             await asyncio.sleep(0.1)                                      # do an await operation to really confirm that we are in async loop
    #             return "it's 42"                                              # return a string so we can confirm execution
    #
    #         return  async_invoke_in_new_loop(an_async_function())             # use async_invoke_in_new_loop to run the async function
    #
    #     assert self.shell.function(execute_in_lambda) == "it's 42"            # get the code of 'execute_in_lambda', send it to AWS Lambda and execute it


    # def test_run_playwright_in_pytest(self):
    #     from osbot_utils.utils.Threads                       import async_invoke_in_new_loop
    #     from osbot_utils.utils.Misc                          import bytes_to_base64
    #     from playwright.async_api                            import async_playwright
    #     from osbot_playwright.playwright.api.Playwright_CLI import Playwright_CLI
    #     playwright_cli = Playwright_CLI()
    #     chrome_path    = playwright_cli.executable_path__chrome()
    #     pprint(chrome_path)
    #
    #     async def get_screenshot(url):
    #
    #         context = await async_playwright().start()
    #         launch_kwargs = dict(args=["--disable-gpu", "--single-process"],
    #                              executable_path=chrome_path)
    #         browser = await context.chromium.launch(**launch_kwargs)
    #
    #         page = await browser.new_page()
    #         await page.goto(url)
    #
    #         screenshot = await page.screenshot(full_page=True)
    #         return bytes_to_base64(screenshot)
    #
    #     result = async_invoke_in_new_loop(get_screenshot("https://www.google.com/404"))

    # def test_invoke_flow_from_pytest(self):
    #     def invoke_flow_from_pytest():
    #         from osbot_serverless_flows.flows.browser.Flow__Playwright__Get_Page_Html import Flow__Playwright__Get_Page_Html
    #         flow__get_page_html = Flow__Playwright__Get_Page_Html()
    #         flow_data           = flow__get_page_html.run()
    #         flow                = flow__get_page_html.flow()
    #
    #         flow.execute_flow()
    #         #
    #         #result = flow.flow_target
    #
    #         # flow_target = flow.flow_target
    #         # flow_args = flow.flow_args
    #         # flow_kwargs = flow.flow_kwargs
    #         # async_coroutine = flow_target(*flow_args, **flow_kwargs)
    #         # #result = async_oroutine
    #         # from osbot_utils.utils.Threads import invoke_in_new_event_loop
    #         # result = invoke_in_new_event_loop(async_coroutine)
    #         result = flow.captured_exec_logs
    #
    #         return f'{result}'
    #
    #     self.shell.function__print(invoke_flow_from_pytest)
    #
    # def test_x_print_misc_query(self):
    #     def misc_query():
    #         from osbot_playwright.playwright.api.Playwright_CLI import Playwright_CLI
    #         playwright_cli = Playwright_CLI()
    #         return playwright_cli.executable_path__chrome()
    #
    #     self.shell.function__print(misc_query)

    # def test_get_environ(self):
    #     def misc_query():
    #         from os import environ
    #         return dict(environ)
    #
    #     self.shell.function__print(misc_query)

