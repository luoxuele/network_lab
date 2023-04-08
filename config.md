git remote set-url --push origin https://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@github.com/luoxuele/network_lab.git
cat .git\config
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        symlinks = false
        ignorecase = true
[remote "origin"]
        url = https://github.com/luoxuele/network_lab.git
        fetch = +refs/heads/*:refs/remotes/origin/*
        pushurl = https://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@github.com/luoxuele/network_lab.git
[branch "main"]
        remote = origin
        merge = refs/heads/main



cat .git\config
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        symlinks = false
        ignorecase = true
[remote "origin"]
        url = https://github.com/luoxuele/network_lab.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
        remote = origin
        merge = refs/heads/main       



git config --global user.name "luoxuele"
git config --global user.email "tianchang1994@gmail.com"
git remote set-url --push origin https://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@github.com/luoxuele/network_lab.git
git remote set-url origin https://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@github.com/luoxuele/network_lab.git

git add . 
git commit -m "update_config"

