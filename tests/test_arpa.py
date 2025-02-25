import filecmp
import os
import os.path
import tempfile

import arpa

TEST_ARPA = os.path.join(os.path.dirname(__file__), "data/test.arpa")


def test_load_dump():
    with open(TEST_ARPA, "rt") as fp:
        lm = arpa.load(fp)[0]
        fp.seek(0)
        with tempfile.TemporaryFile(mode="w+t") as gp:
            arpa.dump(lm, gp)
            gp.seek(0)
            assert fp.read() == gp.read()


def test_loadf_dumpf():
    lm = arpa.loadf(TEST_ARPA)[0]
    out = tempfile.NamedTemporaryFile(mode="w+t", delete=False)
    arpa.dumpf(lm, out.name)
    out.close()
    assert filecmp.cmp(TEST_ARPA, out.name, shallow=False)
    os.unlink(out.name)


def test_loads_dumps():
    with open(TEST_ARPA, "rt") as fp:
        txt = fp.read()
        lm = arpa.loads(txt)[0]
        out = arpa.dumps(lm)
        assert txt == out
