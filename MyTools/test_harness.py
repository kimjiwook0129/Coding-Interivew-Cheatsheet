# Test Harness that I use for solving algorithm problems

def test_harness(fn, tests):
    results = list(map(lambda x: x['result'], tests))
    fn_results = list(map(fn, tests))

    for idx, (result, fn_result) in enumerate(zip(results, fn_results)):
        idx += 1
        if result == fn_result:
            print(f'Test {idx} : Passed')
        else:
            print(f'Test {idx} : Failed')
            print(f'    Test {idx} Actual Result : {result}')
            print(f'    Test {idx} Your Result : {fn_result}')
